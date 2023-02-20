def reverse(s):
    rev=""
    for i in s:
        rev=i+rev
    return rev
#print(reverse("lagnar"))

if __name__=="__main__":
    unittest.main()

