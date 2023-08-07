from module.Action_execution import Action_execution

ACTION = Action_execution.AGGREGATION
TOP_COUNT = 20  # 修改要控管寫入幾個資料排名


def main():
    if ACTION == Action_execution.REPTILE:
        Action_execution.reptile()
    if ACTION == Action_execution.AGGREGATION:
        Action_execution.aggregate(TOP_COUNT)


if __name__ == '__main__':
    main()
