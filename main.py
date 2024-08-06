import random
import string
import progressbar

''' Ask user for total number of emails required'''


def getcount():
    rownums = input("How many email addresses?: ")
    try:
        rowint = int(rownums)
        return rowint
    except ValueError:
        print("Please enter an integer value")
        return getcount()


input_extensions = input('Enter extension(com, net, org, gov): ')
input_domain = input('Enter domain(gmail, yahoo, mail): ')


def makeEmail():
    accountlen = random.randint(1, 20)
    finalacc = ''.join(
        random.choice(string.ascii_lowercase + string.digits)
        for _ in range(accountlen))
    finale = finalacc + "@" + input_domain + "." + input_extensions
    return finale


howmany = getcount()
# counter for While loop
counter = 0
# empty array to add emails
emailarray = []
print("Creating email addresses...")
print("Progress: ")
prebar = progressbar.ProgressBar(maxval=int(howmany))
for i in prebar(range(howmany)):
    while counter < howmany:
        emailarray.append(str(makeEmail()))
        counter += 1
        prebar.update(i)

print("Creation completed.")
for i in emailarray:
    print(i)
