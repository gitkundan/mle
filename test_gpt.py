def find_subsets_divisible_by_k(A, N, K): 
  
    # Create an empty list to store 
    # all the subsets with sum divisible 
    # by K 
    divisible_subsets = [] 
  
    # Get the total no. of subsets 
    total_subsets = 2**N 
  
    # Iterate over total_subsets 
    for subset_index in range(total_subsets): 
  
        # Find the subset 
        bitset = list(bin(subset_index)[2:].zfill(N)) 
  
        # Calculate the sum of the elements 
        # of the subset 
        subset_sum = 0
        for i in range(len(bitset)): 
            if bitset[i] == '1': 
                subset_sum += A[i] 
  
        # Check if the sum is divisible by K 
        if subset_sum % K == 0: 
            divisible_subsets.append(bitset) 
  
    # Print the required result 
    return len(divisible_subsets) 
  
# Driver code 
A = [2, 7, 6, 1, 4] 
K = 3
N = len(A)
  
print("The number of subsets with sum divisible by K is:", 
      find_subsets_divisible_by_k(A, N, K)) 
  
# This code is contributed by Anshika Goyal.