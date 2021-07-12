import time, threading, requests

URL = 'https://api.github.com/repos/{name}/{repo}/commits?page=1&per_page=100'
dict1 = {
    'Zinko17': 'FP',
    'cholponesn': 'StomCentr',
    'aliyaandabekova': 'THE_BEST_PRICE',
    'zhumakova': 'SportBetProject',
}
result = {}

start = time.time()


def worker(username, repository):
    url = URL.format(name=username, repo=repository)
    response = requests.get(url).json()
    length = len(response)
    result[username] = length


ts = []
for key, value in dict1.items():
    t = threading.Thread(target=worker, args=(key, value))
    t.start()
    ts.append(t)

for thread in ts:
    thread.join()

print(time.time() - start)
print(result)


def func(num):
    return num + 10


def my_map(func, iterable):
    for i in iterable:
        yield func(i)


print(list(my_map(func, [1, 23, 4, 56, 3])))
