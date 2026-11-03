import pandas as pd
import os

def generate_mock_data():
    # ==========================================
    # 1. 業務部 (Sales) - dept_sales.xlsx
    # ==========================================
    sales_customers = pd.DataFrame([
        {"customer_id": "C0001", "name": "林怡君", "email": "yijun.lin.test@example.com", "level": "一般", "sales_rep": "直客"},
        {"customer_id": "C0004", "name": "王柏翰", "email": "bohan.wang.test@example.com", "level": "一般", "sales_rep": "直客"},
        {"customer_id": "C0007", "name": "吳欣怡", "email": "hsinyi.wu.test@example.com", "level": "一般", "sales_rep": "直客"},
        {"customer_id": "C0029", "name": "晴川精品旅館", "email": "purchasing.qingchuan.test@example.com", "level": "金級", "sales_rep": "Amy"}
    ])
    
    sales_orders = pd.DataFrame([
        {"order_id": "SO-20260118", "customer_id": "C0001", "order_date": "2026-10-08", "status": "處理中", "total_amount": 32180},
        {"order_id": "SO-20260121", "customer_id": "C0004", "order_date": "2026-10-12", "status": "已出貨", "total_amount": 13205},
        {"order_id": "SO-20260122", "customer_id": "C0007", "order_date": "2026-10-15", "status": "已送達", "total_amount": 9900}
    ])

    sales_order_items = pd.DataFrame([
        {"order_id": "SO-20260118", "sku": "SOF-101", "product_name": "雲朵三人座沙發", "qty": 1, "price": 29800},
        {"order_id": "SO-20260118", "sku": "BED-002", "product_name": "純棉雙人床包", "qty": 1, "price": 2380},
        {"order_id": "SO-20260121", "sku": "APP-055", "product_name": "智慧除濕機", "qty": 1, "price": 13205},
        {"order_id": "SO-20260122", "sku": "APL-201", "product_name": "直立式吸塵器", "qty": 1, "price": 9900}
    ])

    sales_price_list = pd.DataFrame([
        {"sku": "SOF-101", "product_name": "雲朵三人座沙發", "list_price": 29800},
        {"sku": "SOF-201", "product_name": "可收納沙發床", "list_price": 15000},
        {"sku": "BED-002", "product_name": "純棉雙人床包", "list_price": 2380},
        {"sku": "APP-055", "product_name": "智慧除濕機", "list_price": 13205},
        {"sku": "APL-201", "product_name": "直立式吸塵器", "list_price": 9900}
    ])

    sales_support_tickets = pd.DataFrame([
        {"ticket_id": "TK-0901", "customer_id": "C0001", "order_id": "SO-20260118", "issue": "詢問出貨進度", "status": "處理中"}
    ])

    sales_policy = pd.DataFrame([
        {"policy_type": "延遲補償", "description": "訂單延遲出貨時，可提供 5% 購物金補償，或允許客戶免費取消並全額退款。"},
        {"policy_type": "B2B折扣", "description": "金級客戶基礎折扣 12%。單品項訂購超過 30 件，可額外享有 3% 大量加碼折扣。"},
        {"policy_type": "權限", "description": "合計折扣若超過 18%，需標註請執行長核准。"}
    ])

    # ==========================================
    # 2. 營運部 (Ops) - dept_ops.xlsx
    # ==========================================
    ops_products = sales_price_list.copy()
    
    ops_inventory = pd.DataFrame([
        {"sku": "SOF-101", "warehouse": "桃園總倉", "on_hand": 0, "reserved": 0, "available": 0},
        {"sku": "BED-002", "warehouse": "桃園總倉", "on_hand": 50, "reserved": 10, "available": 40},
        {"sku": "SOF-201", "warehouse": "桃園總倉", "on_hand": 12, "reserved": 0, "available": 12},
        {"sku": "SOF-201", "warehouse": "台中倉", "on_hand": 20, "reserved": 0, "available": 20},
        {"sku": "APL-201", "warehouse": "桃園總倉", "on_hand": 15, "reserved": 2, "available": 13}
    ])

    ops_shipments = pd.DataFrame([
        {"order_id": "SO-20260118", "tracking_no": "", "status": "缺貨等待中", "est_delivery": "未定"},
        {"order_id": "SO-20260121", "tracking_no": "TRK998877", "status": "已出貨", "est_delivery": "2026-10-14"},
        {"order_id": "SO-20260122", "tracking_no": "TRK998878", "status": "已送達", "est_delivery": "2026-10-20"}
    ])

    ops_purchase_orders = pd.DataFrame([
        {"po_id": "PO-2026-0312", "sku": "SOF-101", "qty": 30, "current_eta": "2026-11-03", "status": "運送中"},
        {"po_id": "PO-2026-0318", "sku": "SOF-201", "qty": 40, "current_eta": "2026-11-12", "status": "製造中"}
    ])
    
    ops_returns_rma = pd.DataFrame([{"rma_id": "RMA-000", "order_id": "N/A", "status": "N/A"}]) # 預留空表

    ops_policy = pd.DataFrame([
        {"policy_type": "拆單出貨", "description": "若部分商品缺貨，現貨商品可安排先出。第二趟運費由公司吸收。"},
        {"policy_type": "瑕疵退換", "description": "七天鑑賞期內收到瑕疵品，若有庫存可於 2 個工作天內安排換新出貨並到府收回舊機。"},
        {"policy_type": "驗收時間", "description": "採購單 (PO) 到港後，不需額外預留時間，ETA 當日即可出貨。"}
    ])

    # ==========================================
    # 3. 財務部 (Finance) - dept_finance.xlsx
    # ==========================================
    fin_invoices = pd.DataFrame([
        {"order_id": "SO-20260118", "invoice_no": "INV-1001", "amount": 32180, "status": "已開立"},
        {"order_id": "SO-20260121", "invoice_no": "INV-1004", "amount": 13205, "status": "溢收待處理"},
        {"order_id": "SO-20260122", "invoice_no": "INV-1005", "amount": 9900, "status": "已開立"}
    ])

    fin_payments = pd.DataFrame([
        {"order_id": "SO-20260118", "payment_date": "2026-10-08", "amount": 32180, "method": "信用卡"},
        {"order_id": "SO-20260121", "payment_date": "2026-10-12", "amount": 13205, "method": "信用卡"},
        {"order_id": "SO-20260121", "payment_date": "2026-10-12", "amount": 13205, "method": "信用卡(重複)"},
        {"order_id": "SO-20260122", "payment_date": "2026-10-15", "amount": 9900, "method": "信用卡"}
    ])

    fin_refunds = pd.DataFrame([{"refund_id": "REF-000", "order_id": "N/A", "amount": 0, "status": "N/A"}]) # 空表

    fin_credit_accounts = pd.DataFrame([
        {"customer_id": "C0029", "credit_limit": 500000, "outstanding_balance": 150000, "overdue_amount": 50000, "credit_status": "凍結 - 需執行長核准"}
    ])

    fin_product_cost = pd.DataFrame([
        {"sku": "SOF-101", "cost": 12000},
        {"sku": "SOF-201", "cost": 7500},
        {"sku": "BED-002", "cost": 800},
        {"sku": "APP-055", "cost": 8000},
        {"sku": "APL-201", "cost": 5000}
    ])

    fin_policy = pd.DataFrame([
        {"policy_type": "退款時效", "description": "信用卡退刷流程約需 3-7 個工作天入帳。"},
        {"policy_type": "退款權限", "description": "退款金額 NT$10,001 - 50,000 由財務經理核准；超過 NT$50,000 需執行長核准。"},
        {"policy_type": "重複扣款", "description": "確認為溢收或重複扣款時，主動全額退刷溢收金額。"},
        {"policy_type": "B2B信用", "description": "客戶若有逾期帳款且信用狀態為凍結，接新單需先收 50% 訂金或經執行長核准。"},
        {"policy_type": "報價毛利", "description": "報價毛利率若低於 25%，需執行長核准。（內部資料，勿對客戶揭露）"}
    ])

    # 寫出 Excel 檔案
    with pd.ExcelWriter('dept_sales.xlsx') as writer:
        sales_customers.to_excel(writer, sheet_name='customers', index=False)
        sales_orders.to_excel(writer, sheet_name='orders', index=False)
        sales_order_items.to_excel(writer, sheet_name='order_items', index=False)
        sales_price_list.to_excel(writer, sheet_name='price_list', index=False)
        sales_support_tickets.to_excel(writer, sheet_name='support_tickets', index=False)
        sales_policy.to_excel(writer, sheet_name='sales_policy', index=False)

    with pd.ExcelWriter('dept_ops.xlsx') as writer:
        ops_products.to_excel(writer, sheet_name='products', index=False)
        ops_inventory.to_excel(writer, sheet_name='inventory', index=False)
        ops_shipments.to_excel(writer, sheet_name='shipments', index=False)
        ops_purchase_orders.to_excel(writer, sheet_name='purchase_orders', index=False)
        ops_returns_rma.to_excel(writer, sheet_name='returns_rma', index=False)
        ops_policy.to_excel(writer, sheet_name='ops_policy', index=False)

    with pd.ExcelWriter('dept_finance.xlsx') as writer:
        fin_invoices.to_excel(writer, sheet_name='invoices', index=False)
        fin_payments.to_excel(writer, sheet_name='payments', index=False)
        fin_refunds.to_excel(writer, sheet_name='refunds', index=False)
        fin_credit_accounts.to_excel(writer, sheet_name='credit_accounts', index=False)
        fin_product_cost.to_excel(writer, sheet_name='product_cost', index=False)
        fin_policy.to_excel(writer, sheet_name='finance_policy', index=False)

    print("✅ 成功生成 3 個部門的測試資料庫 (Excel)！")

if __name__ == "__main__":
    generate_mock_data()
