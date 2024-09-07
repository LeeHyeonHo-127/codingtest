[ny][nx] = True
            nal = al
            nal.append(board[ny][nx])
            print(ny, " ", nx, " ", nal, " ", nn)
            dq.append(([ny, nx], nal, nn))