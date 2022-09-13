# scan words.txt for words of length 5
# put each letter of those words as an individual element in an array
# count the frequency of each letter

AllFiveLetterWords = []

a_count = 0
b_count = 0
c_count = 0
d_count = 0
e_count = 0
f_count = 0
g_count = 0
h_count = 0
i_count = 0
j_count = 0
k_count = 0
l_count = 0
m_count = 0
n_count = 0
o_count = 0
p_count = 0
q_count = 0
r_count = 0
s_count = 0
t_count = 0
u_count = 0
v_count = 0
w_count = 0
x_count = 0
y_count = 0
z_count = 0

with open('words.txt') as f:
    for line in f:
        if len(line) == 6:
            # OPTIONAL: Have a function check if this is actually a word (no symbols or numbers)
            AllFiveLetterWords.extend(line)

# The problem here is that when you typecast 'line' as a list, each letter becomes its own
# element in a list within a list. We need ONE list, not one list of lists.

# update: the answer was extend()

print(AllFiveLetterWords)

# This one is weird. Why is it only incrementing a_count?

for letters in AllFiveLetterWords:
    if(letters == 'a' or 'A'):
        a_count = a_count + 1
    elif(letters == 'b' or 'B'):
        b_count = b_count + 1
    else:
        z_count = z_count + 1
print(a_count)
print(b_count)
print(z_count)
