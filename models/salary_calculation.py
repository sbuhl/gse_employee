from odoo import models, fields
from odoo.addons.hr_payroll.models import hr_payslip as hr_payslip_module 

import numpy as np
class SalaryCalculation(models.TransientModel):
    _name = 'salary.calculation.wizard'
    _description = 'Salary Calculation Wizard'

    net_salary = fields.Float('Net Salary (USD)')
    basic_salary = fields.Float('Basic Salary (USD)')  
    month = fields.Selection([
        ('january', 'January'),
        ('february', 'February'),
        ('march', 'March'),
        ('april', 'April'),
        ('may', 'May'),
        ('june', 'June'),
        ('july', 'July'),
        ('august', 'August'),
        ('september', 'September'),
        ('october', 'October'),
        ('november', 'November'),
        ('december', 'December'),
    ], string='Month') 

    structure_type_id = fields.Many2one('hr.payroll.structure.type', string="Salary Structure Type") 
    tolerance_threshold = fields.Float('Tolerance Threshold')  
    slip_id = fields.Many2one('hr.payslip', string="Payslip") 
    struct_id = fields.Many2one('hr.payroll.structure', string='Structure')
    rule_ids = fields.One2many(related='struct_id.rule_ids', string="Salary Structure Rules")

    def goalSeek(self,fun,goal,x0,fTol=0.0001,MaxIter=200): 
            if fun(x0)==goal:
                print('Exact solution found')
                return x0

            # Line Search Method
            step_sizes=np.logspace(-1,4,6)
            scopes=np.logspace(1,5,5)

            vFun=np.vectorize(fun)

            for scope in scopes:
                break_nested=False
                for step_size in step_sizes:

                    cApos=np.linspace(x0,x0+step_size*scope,int(scope))
                    cAneg=np.linspace(x0,x0-step_size*scope,int(scope))

                    cA=np.concatenate((cAneg[::-1],cApos[1:]),axis=0)

                    fA=vFun(cA)-goal

                    if np.any(np.diff(np.sign(fA))):

                        index_lb=np.nonzero(np.diff(np.sign(fA)))

                        if len(index_lb[0])==1:

                            index_ub=index_lb+np.array([1])

                            x_lb=np.array(cA)[index_lb][0].item()
                            x_ub=np.array(cA)[index_ub][0].item()
                            break_nested=True
                            break
                        else: # Two or more roots possible

                            index_ub=index_lb+np.array([1])

                            print('Other solution possible at around, x0 = ', np.array(cA)[index_lb[0][1]])

                            x_lb=np.array(cA)[index_lb[0][0]].item()
                            x_ub=np.array(cA)[index_ub[0][0]].item()
                            break_nested=True
                            break

                if break_nested:
                    break
            if not x_lb or not x_ub:
                print('No Solution Found')
                return

            # Bisection Method
            iter_num=0
            error=10

            while iter_num<MaxIter and fTol<error:
                
                x_m=(x_lb+x_ub)/2
                f_m=fun(x_m)-goal

                error=abs(f_m)

                if (fun(x_lb)-goal)*(f_m)<0:
                    x_ub=x_m
                elif (fun(x_ub)-goal)*(f_m)<0:
                    x_lb=x_m
                elif f_m==0:
                    print('Exact spolution found')
                    return x_m
                else:
                    print('Failure in Bisection Method')
                
                iter_num+=1
            print("iter_num", iter_num)
            return x_m
    
    def get_rule_result_formula(self,b):
        # a = ((b*40)/100) + 1622.5;
        # d = 200 + ((12.5 * b)/100); 
        # return b + a - d;
        k = ((b-100000)*0.3) + 8000
        m = b * 0.05
        n = b * 0.03
        p = (b * 0.3)/100
        q = (b * 0.3)/100
        o = ((b - k - n - q) * 0.5)/100
        l = m + n
        u = b - k - n - o - q
        return u

    def calculate_salary(self):
        x0=0.0
        for salary_calculation in self:
            result = self.goalSeek(self.get_rule_result_formula,self.net_salary,x0)
            salary_calculation.basic_salary = abs(result)
            print ("Result: ", result)
        
        for rule in self.rule_ids:
            print("rule", rule.code, rule.amount_python_compute, rule.amount_fix, rule.amount_percentage)

        return {
            'name': 'Salary Calculation',
            'type': 'ir.actions.act_window',
            'res_model': 'salary.calculation.wizard',
            'res_id': self.id,
            'view_mode': 'form',
            'view_id': self.env.ref('gse_employee.view_salary_calculation_wizard_form').id,
            'view_type': 'form',
            'target': 'new',
        }