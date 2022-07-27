from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import query, queryd
stu=FastAPI()
stu.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    
)





@stu.get('/data')
def getting():
    a="data from server"
    return a


@stu.get('/upeg/getRequisitionAgingList')
def getRequisitionAgingList():
    sql_quary="select distinct rd.requisition_id,rd.requisition_title,rd.estimated_value,CONCAT(mu.first_name,' ',mu.last_name) as created_by,rt.req_type, to_char(rd.last_update_date,'DD-MM-YYYY') as last_update_date,rd.delivery_address,rd.billing_address,mtl.l1_name as business_unit,vmvc.item_vendor_category_name as category,to_char(rd.created_date,'DD-MM-YYYY') as created_date,rd.currency FROM upeg.requisition_deails rd JOIN masters.master_user mu ON rd.created_by=mu.user_id JOIN masters.requisition_type rt ON rt.req_type_id=rd.requisition_type JOIN masters.master_tender_l1 mtl ON mtl.tender_l1_id=rd.business_unit JOIN masters.delivery_address da ON da.address_id=rd.billing_address JOIN upeg.requisition_item ri ON ri.requisition_id=rd.requisition_id JOIN masters.view_master_vendor_category vmvc ON vmvc.item_vendor_category_id=ri.category_id ORDER BY created_date DESC"
    # cur.execute("select distinct rd.requisition_id,rd.requisition_title,rd.estimated_value,CONCAT(mu.first_name,' ',mu.last_name) as created_by,rt.req_type,to_char(rd.approved_date,'DD-MM-YYYY') as approved_date,rd.delivery_address,da.address,mtl.l1_name,  vmvc.item_vendor_category_name,to_char(rd.created_date,'DD-MM-YYYY') as created_date,rd.currency FROM upeg.requisition_deails rd  JOIN masters.master_user mu ON rd.created_by=mu.user_id  JOIN masters.requisition_type rt ON rt.req_type_id=rd.requisition_type  JOIN masters.master_tender_l1 mtl ON mtl.tender_l1_id=rd.business_unit JOIN masters.delivery_address da ON da.address_id=rd.billing_address  JOIN upeg.requisition_item ri ON ri.requisition_id=rd.requisition_id JOIN masters.view_master_vendor_category vmvc ON vmvc.item_vendor_category_id=ri.category_id WHERE rd.status=2  ORDER BY created_date DESC")
    result=query(sql_quary)
    return result

