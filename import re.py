import re


def quicksort(quick_List):
    if len(quick_List) <= 1:
        return quick_List
    
    else:
        numArray = quick_List[0]
        sort1 = []
        sort2 = []
        
        for x in range(1, len(quick_List)):
            if quick_List[x] < numArray:
                sort1.append(quick_List[x])
                
            if quick_List[x] > numArray:
                sort2.append(quick_List[x])
                
   
    return quicksort(sort1) + [numArray] + quicksort(sort2)

#Connects code to the number.txt.
def pull_number_txt(readNumbers):
    nums = []
    with open(readNumbers) as file_object:
        numLine = file_object.readLine()
        fileNumbers = re.findall("[0-9]+", numLine)
        
        for n in fileNumbers:
            n = int(n)
            nums.append(n)
    return nums

#result output
def write_sorted_txt(writeSorted, fileNumbers):
    with open(writeSorted, "w") as sorted_numbers:
        for i in quicksort(fileNumbers):
            i = str(i)
            sorted_numbers.write(f"{i}\n")
            
#GIVEN: main function for running the program
def main():
    fileNumbers = pull_number_txt("C:\Users\harry\Downloads\numbers.txt") 
    
    return write_sorted_txt("C:\Users\harry\Downloads\numbers.txt", fileNumbers) 

#GIVEN:
if __name__ == "__main__":
    main()