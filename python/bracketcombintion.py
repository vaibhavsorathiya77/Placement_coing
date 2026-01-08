def BracketCombinations(num):
    def count(open_count, closed_count):
      if open_count == num and closed_count == num:
        return 1
      total = 0

      if open_count < num:
        total += count(open_count+1,closed_count)

      if closed_count< open_count:
        total+= count(open_count,closed_count+1)
      return total

    return count(0,0)

# keep this function call here 
print(BracketCombinations(input(9)))