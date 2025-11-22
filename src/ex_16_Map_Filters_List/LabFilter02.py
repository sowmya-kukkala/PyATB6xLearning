test_results = ["PASS", "FAIL", "PASS", "SKIP", "FAIL"]

pass_results_only = list(filter(lambda x : x=="PASS", test_results))
print(pass_results_only) # ['PASS', 'PASS']


list_student = [50, 51, 100]

def keep(x):
    if x > 50:
        return x

students_with_eligiblity = list(filter(keep, list_student))
print(students_with_eligiblity) # [51, 100]
