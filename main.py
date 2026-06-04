def calculate_discount(order: dict) -> float:
    """
    计算订单实际支付金额。

    规则：
    - VIP 用户打 9 折
    - 满 100 元减 20 元
    - 优惠券不能叠加（如果有优惠券，则不再使用满减）

    Args:
        order: 订单信息，包含:
            - amount: 订单金额
            - is_vip: 是否为 VIP 用户
            - has_coupon: 是否有优惠券

    Returns:
        实际支付金额
    """
    amount = order.get("amount", 0)
    is_vip = order.get("is_vip", False)
    has_coupon = order.get("has_coupon", False)

    # 优惠券优先级最高，有优惠券则不使用满减
    if has_coupon:
        final_amount = amount
    else:
        # 满 100 减 20（可多次叠加）
        final_amount = amount - (amount // 100) * 20

    # VIP 折扣在最后应用
    if is_vip:
        final_amount *= 0.9

    return round(final_amount, 2)


def main():
    # 测试用例
    test_cases = [
        {"amount": 150, "is_vip": False, "has_coupon": False},  # 满减: 150-20=130
        {"amount": 150, "is_vip": True, "has_coupon": False},   # VIP+满减: 150*0.9=135, 再满减无剩余
        {"amount": 150, "is_vip": True, "has_coupon": True},    # VIP+优惠券: 150*0.9=135
        {"amount": 250, "is_vip": False, "has_coupon": False},  # 满减两次: 250-40=210
        {"amount": 80, "is_vip": False, "has_coupon": False},   # 不满100，无满减: 80
    ]

    for tc in test_cases:
        result = calculate_discount(tc)
        print(f"订单: {tc} -> 实际支付: {result}")


if __name__ == "__main__":
    main()
