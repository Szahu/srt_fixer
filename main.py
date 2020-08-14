_subitilesFile = open("subtitles.srt", "r")
_newFile = open("fiexd_subtitles.srt", "w")

for line in _subitilesFile:
    line_list = list(line)  
    _toEdit = False
    _firstDashIndex = 0

    _firstDashIndex = line.find("-->")

    if _firstDashIndex != -1:
        _toEdit = True

    if _toEdit:
           
        line_list[_firstDashIndex - 5] = ''
        line_list[_firstDashIndex + 13] = ''
        newLine = "".join(line_list)
        _newFile.write(newLine)


    else:
        _newFile.write(line)
                   
