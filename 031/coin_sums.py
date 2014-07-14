VALUE = 200

def is_solution_and_is_greater(a, b, c, d, e, f, g, h):
  sigma = a*200 + b*100 + c*50 + d*20 + e*10 + f*5 + g*2 + h
  return sigma == VALUE, sigma > VALUE

solutions = []
for a in range(0, 2): #200
  if is_solution_and_is_greater(a, 0, 0, 0, 0, 0, 0, 0)[1]:
    break
  for b in range(0, 3): #100
    if is_solution_and_is_greater(a, b, 0, 0, 0, 0, 0, 0)[1]:
      break
    for c in range(0, 5): #50
      if is_solution_and_is_greater(a, b, c, 0, 0, 0, 0, 0)[1]:
        break
      for d in range(0, 11): #20
        if is_solution_and_is_greater(a, b, c, d, 0, 0, 0, 0)[1]:
          break
        for e in range (0, 21): #10
          if is_solution_and_is_greater(a, b, c, d, e, 0, 0, 0)[1]:
            break
          for f in range(0, 41): #5
            if is_solution_and_is_greater(a, b, c, d, e, f, 0, 0)[1]:
              break
            for g in range(0, 101): #2
              if is_solution_and_is_greater(a, b, c, d, e, f, g, 0)[1]:
                break
              for h in range(0, 201): #1
                is_solution, is_greater = is_solution_and_is_greater(
                  a, b, c, d, e, f, g, h)
                if is_greater: 
                    break
                elif is_solution:
                  solutions.append([a, b, c, d, e, f, g, h])

print len(solutions)
