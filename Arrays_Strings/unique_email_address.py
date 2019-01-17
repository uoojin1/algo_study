'''
Every email consists of a local name and a domain name, separated by the @ sign.
For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.
Besides lowercase letters, these emails may contain '.'s or '+'s.
If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)
If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)
It is possible to use both of these rules at the same time.
Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails?

'''

# def numUniqueEmails(emails):
#     seen = set()
#     for email in emails:
#         local, domain = email.split('@')
#         cleanLocal = local.split('+')[0].replace('.','')
#         totalEmail = cleanLocal + '@' + domain
#         seen.add(totalEmail)
#     return len(seen)

# testinput = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

# print numUniqueEmails(testinput)

# []
# ['a@b.com']
# ['a@b.com', 'a@b.co.m']
# ['a@b.com', 'a.@b.co.m', '@b.com', '.a@b.com']

def solution(L):
    # write your code in Python 3.6
    if not L:
        return 0
    seenEmails = {}
    emailWithMaxCount = ''
    maxCount = 0
    for email in L:
        localPart, domainPart = email.split('@')
        localClean = localPart.split('+')[0]
        localCleanWithoutDot = localClean.replace('.','')
        processedEmail = localCleanWithoutDot + '@' + domainPart
        print 'processedEmail', processedEmail
        if processedEmail in seenEmails:
            seenEmails[processedEmail] += 1
            if seenEmails[processedEmail] > maxCount:
                maxCount = seenEmails[processedEmail]
        else:
            seenEmails[processedEmail] = 1
            if seenEmails[processedEmail] > maxCount:
                maxCount = seenEmails[processedEmail]
    return maxCount

print solution(['aaa@b.com', 'a.a.a@b.co.m', 'aa+a@b.com', 'a.aa+.a@b.com'])


['aaa@b.com', 'a.a.a@b.co.m', 'aa+a@b.com', 'a.aa+.a@b.com']

# def solution(L):
#     # write your code in Python 3.6
#     if not L:
#         return 0
#     seenEmails = {}
#     emailWithMaxCount = ''
#     maxCount = 0
#     for email in L:
#         localPart, domainPart = email.split('@')
#         localClean = localPart.split('+')[0].replace('.', '')
#         processedEmail = localClean + '@' + domainPart
#         if processedEmail in seenEmails:
#             seenEmails[processedEmail] += 1
#             if seenEmails[processedEmail] > maxCount:
#                 maxCount = seenEmails[processedEmail]
#         else:
#             seenEmails[processedEmail] = 1
#             if seenEmails[processedEmail] > maxCount:
#                 maxCount = seenEmails[processedEmail]
#     return maxCount
    