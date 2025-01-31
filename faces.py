def convert(input):
    if ":)" in input:
        input = "smile"
        return input
    elif ":(" in input:
        input = "frown"
        return input
    else:
        return input 
    
def main():
    e = input("Enter an emoticon: ")
    result = convert(e)
    print(result)
    
    
main()