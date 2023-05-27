class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        node = ListNode(value)
        current.next = node
        current = current.next

    return head


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def main():
    values = [1, 2, 3, 4, 5, 6]
    head = createLinkedList(values)

    current = head

    while current:
        print(current.val)
        current = current.next

    print(has_cycle(head))


if __name__ == "__main__":
    main()
