import regex as re

a="Angeline Kingsteena"
stringy=re.findall(r"""(((?<=A)[^\s]*)) #to find words between A and space
((?<= )[^a].)  #"""  ,a,re.VERBOSE)
# re.search(r'(?<=SLA_)[^_]*',str)
stringy

#[('ngeline', 'ngeline', ' K')]