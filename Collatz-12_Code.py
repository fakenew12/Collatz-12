#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Duodecadia: Collatz-12 Dynamical System
# © Hiroshi Harada 2026 — Released under CC BY 4.0

def step12(n):
    r = n % 12
    if r == 0:  return n // 12
    elif r == 1:  return 13 * n - 1
    elif r == 2:  return n // 2
    elif r == 3:  return n // 3
    elif r == 4:  return n // 4
    elif r == 5:  return 13 * n + 7
    elif r == 6:  return n // 6
    elif r == 7:  return 13 * n + 5
    elif r == 8:  return n // 4
    elif r == 9:  return n // 3
    elif r == 10: return n // 2
    elif r == 11: return 13 * n + 1
    return n

def analyze_duodecadia(n0, max_steps=2000):
    n = n0
    peak = n
    steps = 0
    rim_hits = {1: 0, 5: 0, 7: 0, 11: 0}

    while steps < max_steps and n != 1:
        r = n % 12
        if r in rim_hits:
            rim_hits[r] += 1

        n = step12(n)
        peak = max(peak, n)
        steps += 1

    return {
        "start": n0,
        "steps": steps,
        "peak": peak,
        "rim_hits": rim_hits
    }

def main():
    print("=== Duodecadia: Collatz-12 Sanctuary Explorer ===")
    n0 = int(input("Enter a positive integer: "))

    result = analyze_duodecadia(n0)

    print("\n--- Result ---")
    print(f"Start Value : {result['start']}")
    print(f"Steps       : {result['steps']}")
    print(f"Peak Value  : {result['peak']}")
    print(f"Rim Hits    : {result['rim_hits']}")
    print("\nClass 7 hits (Sanctuary):", result["rim_hits"][7])

if __name__ == "__main__":
    main()


# In[ ]:




