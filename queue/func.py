from queue_lesson import Queue


def rotate(q: Queue, N: int):
    """'Вращает' очередь по кругу на N элементов."""

    if not isinstance(q, Queue):
        raise ValueError("The first argument must be of the Queue type.")

    if not isinstance(N, int):
        raise ValueError("The second argument must be of the integer type.")

    if N < 0:
        return

    if N > q.size():
        N = N % q.size()

    if N == 0:
        return

    while N > 0:
        q.enqueue(q.dequeue())
        N -= 1
