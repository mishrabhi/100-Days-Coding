# After IOI Ilya decided to make a business. He found a social network called "TheScorpyBook.com". It currently has N registered users. As in any social network two users can be friends. Ilya wants the world to be as connected as possible, so he wants to suggest friendship to some pairs of users. He will suggest user u to have a friendship with user v if they are not friends yet and there is a user w who is friends of both of them. Note that u, v and w are different users. Ilya is too busy with IPO these days, so he asks you to count how many friendship suggestions he has to send over his social network.

t=int(input())
l=[]
l1=[]
for i in range(t):
    s=input()
    l.append(s)
    l1.append(int(s,2))
j=0
k=0
cout=0
while(j<t-1):
    k=j+1
    while(k<t):
        if(l[j][k]=="0" and (l1[j]&l1[k]>=1)):
            cout=cout+2
        k=k+1
    j=j+1
print(cout)