def reader(data):
    #cadena_test = "Robert0000000Smith000123"
    control = 0
    name = ""
    last_name = ""
    id = ""
    pos = []
    sub_pos_1 = []
    sub_pos_2 = []

    for i in range(len(data)):
        print(data[i])
        if data[i] == "0":
            pos.append(i)
    print(pos)
    for a in range(len(pos)):
        print(f"El for va en{pos[a]}")
        print(control)
        try:
            if pos[a] == pos[a + 1] - 1 and control == 0:
                sub_pos_1.append(pos[a])
                print(sub_pos_1)
            elif control == 0 and pos[a] != pos[a + 1] - 1:
                control = 1
                sub_pos_1.append(pos[a])
        except:
            pass
        try:
            if pos[a] == pos[a + 1] - 1 and control == 1:
                sub_pos_2.append(pos[a + 1])
            elif control == 1 and pos[a] != pos[a + 1] - 1:
                sub_pos_2.append(pos[a + 1])
        except:
            pass

    print(f"Sub_pos_1: {sub_pos_1} y Sub_pos_2: {sub_pos_2}")

    # "Robert000Smith000123"
    control = 0
    try:
        for b in data:
            print(b)
            print(sub_pos_1[-1], sub_pos_2[0])
            if control < sub_pos_1[0]:
                name += b
            if control > sub_pos_1[-1] and control < sub_pos_2[0]:
                last_name += b
            if control > sub_pos_2[-1]:
                id += b
            control += 1
    except:
        pass
    print(name)
    print(last_name)
    print(id)
    decrypted = {}
    decrypted = {"first_name" : name, "last_name": last_name, "id": id}
    return decrypted
