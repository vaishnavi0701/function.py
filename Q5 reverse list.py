# def reverse_list():
#     alphabet = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
#     a=reversed(alphabet)
#     l=[]
#     i=0
#     for i in a:
#         l.append(i)
#     print(l)
# reverse_list()

def reverse_list():
    alphabet = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
    i=0
    while i<len(alphabet):
        i=i+1
    print(alphabet[::-1])
reverse_list()