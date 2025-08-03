# Tuples in Python

What is a Tuple?
A tuple is like a list, but with a key difference — tuples are immutable, meaning you can’t change their content after they’re created.

✔️ Use them when the data should not be modified
✔️ Great for grouping related values (e.g., coordinates, configurations)

```python
my_tuple = (1, 2, 'apple', 'banana')
```

---

## Mini Use-Case 
Tuples are great when returning structured data that shouldn't change:
```python
def get_server_info():
    return ('192.168.0.1', 8080)

ip, port = get_server_info()
print(f"Connect to {ip} on port {port}")
```