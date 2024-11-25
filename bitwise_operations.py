import sys
# this is feature1


def validate_and_parse_input(input_data):
    
    
    try:
        numbers = [int(n) for n in input_data.split(",")]
        return numbers
    except ValueError:
        raise ValueError("All input values must be integers separated by commas.")

def bitwise_operations(numbers):
    
    
    bitwise_and = numbers[0]
    bitwise_or = numbers[0]
    bitwise_xor = numbers[0]

    for num in numbers[1:]:
        bitwise_and &= num
        bitwise_or |= num
        bitwise_xor ^= num

    return bitwise_and, bitwise_or, bitwise_xor

def filter_numbers(numbers, threshold):
    
    return [num for num in numbers if num > threshold]

def main():
    if len(sys.argv) != 3:
        print("<p>Error: Two inputs are required (integers and threshold).</p>")
        return

    integers_input = sys.argv[1]
    try:
        threshold = int(sys.argv[2])
    except ValueError:
        print("<p>Error: Threshold must be an integer.</p>")
        return

    try:
        numbers = validate_and_parse_input(integers_input)
    except ValueError as e:
        print(f"<p>Error: {e}</p>")
        return

    and_result, or_result, xor_result = bitwise_operations(numbers)

    filtered_numbers = filter_numbers(numbers, threshold)

    print("<p>Bitwise AND: {}</p>".format(and_result))
    print("<p>Bitwise OR: {}</p>".format(or_result))
    print("<p>Bitwise XOR: {}</p>".format(xor_result))
    print("<p>Numbers greater than threshold ({}): {}</p>".format(threshold, filtered_numbers))

if __name__ == "__main__":
    main()