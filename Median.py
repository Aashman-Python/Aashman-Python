def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    return median

def main():
    numbers = []
    while True:
        try:
            num = input("Enter a number (or type 'done' to finish): ")
            if num.lower() == 'done':
                break
            numbers.append(float(num))
        except ValueError:
            print("Please enter a valid number.")
    
    if numbers:
        median = calculate_median(numbers)
        print(f"The median is: {median}")
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()