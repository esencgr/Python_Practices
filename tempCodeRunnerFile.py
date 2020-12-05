    # clean lisr and file 
    lst.clear()
    file.seek(0)
    file.writelines(lst)
    print(lst)
