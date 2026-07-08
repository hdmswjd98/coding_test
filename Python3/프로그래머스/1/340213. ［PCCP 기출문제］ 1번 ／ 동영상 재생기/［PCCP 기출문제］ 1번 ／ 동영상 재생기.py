def ToSec(tt):
	mm, ss = int(tt[0:2]), int(tt[3:5])
	return mm*60 + ss

def ToStr(tt):
	mm, ss = tt //60, tt % 60
	tt = f"{mm:02d}:{ss:02d}"
	return tt

def Check(tar, st, ed):
	if ((tar >=st) and (tar <=ed)):
		return ed
	else:
		return tar
	
def solution(video_len, pos, op_start, op_end, commands):
	L = ToSec(video_len)
	pos = ToSec(pos)
	st = ToSec(op_start)
	ed = ToSec(op_end)
	pos = Check(pos, st, ed)
	for i in range(len(commands)):
		if ( commands[i] == "next"):
			pos = min(pos+10, L)
		else:
			pos = max(pos-10, 0)
		pos = Check(pos, st, ed)
	answer = ToStr(pos)
	return answer

print(solution("34:33", "13:00", "00:55",	"02:55", ["next", "prev"]))
print(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"]))
print(solution("07:22", "04:05", "00:15", "04:07", ["next"]))