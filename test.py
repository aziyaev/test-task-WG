import unittest
import CyclesBufferList_task2 as list_method
import CyclesBufferQueue_task2 as queue_method

class TestCyclesBuffer(unittest.TestCase):
    def testQueue(self):
        queue = queue_method.CyclesBuffer(4)
        queue.push(3)
        queue.push(100)
        queue.push(1)
        queue.push(100)

        try:
            queue.push(7)
        except Exception:
            self.assertTrue(True)

        self.assertEqual(queue.pop(), 3)
        self.assertEqual(queue.pop(), 100)
        self.assertEqual(queue.pop(), 1)
        self.assertEqual(queue.pop(), 100)

        try:
            queue.pop()
        except Exception:
            self.assertTrue(True)



    def testList(self):
        list = list_method.CyclesBuffer(5)
        list.push(3)
        list.push(100)
        list.push(1)
        list.push(100)

        try:
            list.push(7)
        except Exception:
            self.assertTrue(True)

        self.assertEqual(list.pop(), 3)
        self.assertEqual(list.pop(), 100)
        self.assertEqual(list.pop(), 1)
        self.assertEqual(list.pop(), 100)

        try:
            list.pop()
        except Exception:
            self.assertTrue(True)





if __name__ == "__main__":
    unittest.main()