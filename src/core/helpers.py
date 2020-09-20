#
# helpers.py
#
# the pashmak project
# Copyright 2020 parsa mpsh <parsampsh@gmail.com>
#
# This file is part of pashmak.
#
# pashmak is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pashmak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pashmak.  If not, see <https://www.gnu.org/licenses/>.
##################################################

''' Partial of program object functions '''

from core import commands

class Helpers(commands.Commands):
    ''' Partial of program object functions '''
    
    def raise_variable_error(self , varname , op):
        ''' Raise variable not found error '''
        return self.raise_error('VariableError' , 'undefined variable "' + str(varname) + '"' , op)

    def raise_syntax_error(self , string , op):
        ''' Raises syntax error '''
        return self.raise_error('SyntaxError' , 'unexpected "' + string + '"' , op)

    def arg_should_be_variable(self , arg , op):
        ''' Checks argument syntax is variable name '''
        if arg[0] != '$':
            self.raise_syntax_error(arg[0] , op)

    def arg_should_be_variable_or_mem(self , arg , op):
        ''' Checks argument syntax is variable name or mem '''
        if arg[0] != '$' and arg != '^':
            self.raise_syntax_error(arg[0] , op)

    def variable_exists(self , varname):
        ''' Checks a variable is exists or not '''
        try:
            tmp = self.variables[varname]
            return True
        except:
            return False

    def variable_required(self , varname , op):
        ''' Raises variable error if variable not exists '''
        if not self.variable_exists(varname):
            self.raise_variable_error(varname , op)

    def require_one_argument(self , op , error_message):
        if len(op['args']) <= 0:
            self.raise_error('ArgumentError' , error_message , op)