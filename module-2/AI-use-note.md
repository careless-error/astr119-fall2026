# HW 2 Loopapalooza AI use note
# Part 1 Legendre Polynomials
Prediction:
    The formula for a 2nd degree Legendre Polynomial is P2(x)=(3x^2-1)/2
    for x = 0.5, P2(0.5) = -0.125
    So, legpoly(2, 0.5) should return -0.125

# AI Assistance
input:
    we need to create a loop that starts with P_0(x)=1 and P_1(x) = x
    then use the recurrence relation 
    (n + 1)P_{n+1}(x) = (2n + 1)xP_n(x) - nP_{n-1}(x) 
    to calculate values until it reached P_n(x). 
    Only modify legpoly()
claude output:
    # Calculate P_n(x)
    # TODO(human): compute P_n(x) with a loop, no recursive calls.
    #   1. Start with the two known values: P_0(x) = 1 and P_1(x) = x.
    #   2. Handle n = 0 and n = 1 (the answer is already one of those two).
    #   3. Loop k = 1, 2, ..., n-1. Each pass computes
    #          P_{k+1} = ((2k + 1) * x * P_k - k * P_{k-1}) / (k + 1)
    #   4. After each pass, shift: old P_k becomes P_{k-1}, new value becomes P_k.
    #   5. When the loop ends, set y to P_n.

    This just kind of restated what I asked it to do without giving me any real guidance. 
    
    I asked claude why it ends with k-1 and not n. and it explained that range(1, n) will give the last term of n-1

    Asked how to start the loop and claude gave me for k in range(1, n): and reminded me to define my variables first

# Changes made by hand
    I wrote the loop based on claude's suggestion. VScode wanted me to use an elif but that was redundant so I just used if and else since it only matters if n is 0 and for all other instances we will set y to p_curr

# Testing and verification 
    claude caught that I forgot to get rid of the y = none 
    I ran legendre.py and all values were correct

# Problems Encountered
    Just some basic typos on my end and claude being a little too verbose which can make it a little hard to follow. 

# Part 2 multitab.py
    I wrote teh loop by myself and only asked claude to check my work. No issues found

