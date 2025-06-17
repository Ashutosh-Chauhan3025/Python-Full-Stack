from collections import deque
logs = [
    "[2025-06-16T10:00:00] INFO user1: Started process",
    "[2025-06-16T10:00:01] ERROR user1: Failed to connect",
    "[2025-06-16T10:00:02] INFO user2: Login successful",
    "[2025-06-16T10:00:03] WARN user3: Low memory",
    "[2025-06-16T10:00:04] ERROR user2: Timeout occurred",
    "[2025-06-16T10:00:05] INFO user1: Retrying connection"
]
d = deque(maxlen=2)
d1 = {}
def add_log(log:str)->None:
    log=log.split(" ")
    d.append(log)
    user=log[2]
    user=user[:len(user)-1]
    d1[user]={"Timestamp":log[0],"Frequency":log[1]}



for l in logs:
    add_log(l)
print(d)
print(d1)