'''
1.Recursion - a way of solving a problem by having a function calling itself
    - can generally be solved by iteration
    - example: Russian Doll
    - performing the same operation multiple times with different inputs
    - in every step, we try smaller inputs to make the problem smaller
    - base condition is needed to stop the recursion, otherwise infinite loop will occur

    def open_russian_doll(doll):
        if doll == 1:
            print('All dolls are opened')
        else:
            open_russian_doll(doll-1)

    1.1.why recursion:
        - recursive thinking helps break down big problems into small ones and easier to use
        - recursive code is easier to write than loops
        - used in data structures like trees and graphs
'''