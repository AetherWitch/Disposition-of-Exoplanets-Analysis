import matplotlib.pyplot as plt

file = open("disposition.csv", "r")
dataIn = file.read()
file.close() 
myList = dataIn.split("\n")

# Pre-processing
for item in myList:
    if item == "koi_disposition":
        myList.remove(item) 

# -------------Analysis-----------------
# Frequency
confirmed = ["CONFIRMED"]
falsepos = ["FALSE POSITIVE"]
candidate = ["CANDIDATE"]
nd = ["NOT DISPOSITIONED"]
words = []
wordcount = []

# counting and printing
for word in confirmed:
    confirmCount = myList.count(word)
print("frequency of confirmed exoplanets: ", confirmCount)

for word in falsepos:
    falseCount = myList.count(word)
print("frequency of false positive exoplanets: ", falseCount)

for word in candidate:
    candidateCount = myList.count(word)
print("frequency of candidates: ", candidateCount)

# maybe remove
for word in nd:
    notd = myList.count(word)
print("frequency of not dispositioned exoplanets: ", notd)

total = int(confirmCount)+int(falseCount)+int(candidateCount)
print("total frequency of dispositions", total)

# Median
middle = len(myList)//2
median = myList[middle]
print("the median is ", median)

# Mean
mean = total/3
print("the mean of the dispositions is: ", mean)

# The maximum and minimum values
myList.sort()

minValue = myList[2]
maxValue = myList[-1]

print("This is the min value: ", minValue) 
print("This is the max value: ", maxValue) 

for item in myList:
    if item not in words:
        words.append(item)

for word in words:
    total = myList.count(word)
    wordcount.append(total)

# Mode
maxFrequency = max(wordcount)
maxFrequencyIndex = wordcount.index(maxFrequency)
mode = words[maxFrequencyIndex]
print("the mode is ", mode)

print("")
print("This data is also available on a text file")

# Pie chart
activities = ['confirmed', 'false positive', 'candidate']

slices = [confirmCount, falseCount, candidateCount]

colors = ['#5BCEFA', '#F5A9B8', '#ffffff']

plt.pie(slices, labels=activities, colors=colors, startangle=90, radius=1.2, autopct='%1.1f%%')

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.legend()
plt.show()

# Bar chart
left = [1, 2, 3]

height = [candidateCount, confirmCount, falseCount]

tick_label = ['candidate', 'confirmed', 'false positive'] 

plt.bar(left, height, tick_label=tick_label, width=0.8, color=['#ffcccc', '#ff80bf', '#ff9933'])

plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
plt.title('dispositions of exoplanet candidates') 

plt.show()

# opening a text file
file = open("The Results.txt", "w")
file.write("Total frequency of dispositions: 9564 \n The frequency of confirmed exoplanets: 2293 \n "
           "The frequency of false positives: 5023 \n The frequency of candidates: 2248 \n "
           "The mean of the dispositions: 3188 \n The mode of the dispositions: false positive \n"
           " The median of the dispositions: confirmed \n"
           "The disposition that has the highest frequency(maximum value): false positive \n "
           "The disposition that has the lowest frequency(minimum value): candidate \n")
file.close()
