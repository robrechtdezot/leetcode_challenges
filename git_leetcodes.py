def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ''' sort and get first and last string + minimal length'''
        strs.sort()
        first = strs[0]
        last = strs[-1]
        min_len = min(len(first), len(last))

        '''itterate until first and last are not equal'''
        i = 0
        while i < min_len and first[i] == last[i]:
            i+=1      
            if i == 0: 
                return ''
        return first[:i]
        
def isBalanced(s):
  
    # Declare a stack to store the opening brackets
    st = []
    for i in range(len(s)):
        
        # Check if the character is an opening bracket
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            st.append(s[i])
        
        else:
            # If it's a closing bracket, check if the stack is non-empty
            # and if the top of the stack is a matching opening bracket
            if st and ((st[-1] == '(' and s[i] == ')') or 
                       (st[-1] == '{' and s[i] == '}') or
                       (st[-1] == '[' and s[i] == ']')):

                # Pop the matching opening bracket
                st.pop()
            else:
                # Unmatched closing bracket
                return False

    # If stack is empty, return True (balanced), otherwise False
    return not st
def isValid(self, s: str) -> bool:
        # Initialize an empty list to use as a stack
        stack = []
        # Create a set with valid parentheses pairs
        valid_pairs = {'()', '[]', '{}'}
        # Iterate over each character in the string
        for char in s:
            # If the character is an opening parenthesis, push it onto the stack
            if char in '({[':
                stack.append(char)
            # If the stack is empty or the formed pair is not valid, return False
            elif not stack or stack.pop() + char not in valid_pairs:
                return False
        # If the stack is empty, all parentheses were valid and correctly nested

        return not stack    

def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = curr = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                curr.next, list1 = list1, list1.next
            else:
                curr.next, list2 = list2, list2.next
            curr = curr.next
        curr.next = list1 or list2
        return head.next
        # dummy = ListNode()
        # tail = dummy

        # while list1 and list2:
        #     if list1.val < list2.val:
        #         tail.next, list1 = list1, list1.next
        #     else:
        #         tail.next, list2 = list2, list2.next
        # tail = tail.next
        # if list1:
        #     tail.next = list1
        # elif list2:
        #     tail.next = list2
        # return dummy.next
        # merged = []
        # for i in list1:
        #     for j in list2:
        #         if list1[i] < list2[j]:
        #             merged.append(list1[i])
        #         else:
        #             merged.append(list2[j])
        # return merged         