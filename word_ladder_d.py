#https://leetcode.com/problems/word-ladder-ii/description/
"""
realization #4
leetcode: 39/39 accepted
test "nanny" -> "aloud": ~0.1 sec

algorithm: recursive double BFS 
details: store tree in collections.defaultdict(list): 'word' -> ['next_word_1',...,'next_word_k']
"""
import sys
import collections
import string
import time

def output(curr, end, tree):
	if curr == end: return [[end]]
	return [[curr] + path for each in tree[curr] for path in output(each, end, tree)]

def add_path(word, next_word, tree, flag):
	if not flag:
		tree[word] += [next_word]
	else:
		tree[next_word] += [word]

def new_words(word, word_set):
	for l in range(len(word)):
		for letter in string.ascii_lowercase:
			new_word = word[:l] + letter + word[l+1:]
			if new_word in word_set:
				yield new_word

def double_bfs(curr_lvl, other_lvl, tree, is_reversed, word_set):
	if not curr_lvl: return False
	if len(curr_lvl) > len(other_lvl):
		return double_bfs(other_lvl, curr_lvl, tree, not is_reversed, word_set)

	word_set = word_set - curr_lvl - other_lvl
	new_lvl, done = set(), False
	while curr_lvl:
		word = curr_lvl.pop()
		for next_word in new_words(word, word_set | other_lvl):
			if next_word in other_lvl:
				done = True
				add_path(word, next_word, tree, is_reversed)
			if not done:
				new_lvl.add(next_word)
				add_path(word, next_word, tree, is_reversed)
	return done or double_bfs(new_lvl, other_lvl, tree, is_reversed, word_set)

def input_txt():
	with open("input.txt", "r") as f:	
		begin_word = f.readline().strip()
		end_word = f.readline().strip()
		word_list = [word for word in f.readline().strip().split(" ")]
	return begin_word, end_word, word_list
begin_word, end_word, word_list = input_txt()
#begin, end, word_list = "hit", "cog", ["hot","dot","dog","lot","log"]

tac = time.time()

word_set = set(word_list)
tree = collections.defaultdict(list)
if end_word in word_set:
	double_bfs({begin_word}, {end_word}, tree, False, word_set)
	print(output(begin_word, end_word, tree))
else:
	print([])

tic = time.time()
print(f"Time : {tic - tac} sec")

