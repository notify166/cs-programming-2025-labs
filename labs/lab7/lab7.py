objects=[("Containment Cell A",4),("Archive Vault",1),("Bio Lab Sector",3),("Observation Wing",2)]
sorted_objects=sorted(objects,key=lambda item:item[1])
print(sorted_objects)


staff_shifts=[{"name":"Dr. Shaw","shift_cost":120,"shifts":15},{"name":"Agent Torres","shift_cost":90,"shifts":22},{"name":"Researcher Hall","shift_cost":150,"shifts":10}]
total_costs=list(map(lambda s:{"name":s["name"],"total":s["shift_cost"]*s["shifts"]},staff_shifts))
max_cost=max(total_costs,key=lambda x:x["total"])
print(total_costs)
print(max_cost)


personnel=[{"name":"Dr. Klein","clearance":2},{"name":"Agent Brooks","clearance":4},{"name":"Technician Reed","clearance":1}]
def category(level):
    if(level==1):
        return"Restricted"
    if(2<=level<=3):
        return"Confidential"
    return"Top Secret"
personnel_with_category=list(map(lambda p:{"name":p["name"],"clearance":p["clearance"],"category":category(p["clearance"])},personnel))
print(personnel_with_category)


zones=[{"zone":"Sector-12","active_from":8,"active_to":18},{"zone":"Deep Storage","active_from":0,"active_to":24},{"zone":"Research Wing","active_from":9,"active_to":17}]
day_zones=list(filter(lambda z:z["active_from"]>=8 and z["active_to"]<=18,zones))
print(day_zones)


reports=[{"author":"Dr. Moss","text":"Analysis completed. Reference: http://external-archive.net"},{"author":"Agent Lee","text":"Incident resolved without escalation."},{"author":"Dr. Patel","text":"Supplementary data available at https://secure-research.org"},{"author":"Supervisor Kane","text":"No anomalies detected during inspection."},{"author":"Researcher Bloom","text":"Extended observations uploaded to http://research-notes.lab"},{"author":"Agent Novak","text":"Perimeter secured. No external interference observed."},{"author":"Dr. Hargreeve","text":"Full containment log stored at https://internal-db.scp"},{"author":"Technician Moore","text":"Routine maintenance completed successfully."},{"author":"Dr. Alvarez","text":"Cross-reference materials: http://crosslink.foundation"},{"author":"Security Officer Tan","text":"Shift completed without incidents."},{"author":"Analyst Wright","text":"Statistical model published at https://analysis-hub.org"},{"author":"Dr. Kowalski","text":"Behavioral deviations documented internally."},{"author":"Agent Fischer","text":"Additional footage archived: http://video-storage.sec"},{"author":"Senior Researcher Hall","text":"All test results verified and approved."},{"author":"Operations Lead Grant","text":"Emergency protocol draft shared via https://ops-share.scp"}]
reports_with_links=list(filter(lambda r:("http://" in r["text"]) or ("https://" in r["text"]),reports))
def sanitize_text(t):
    parts=t.split(" ")
    for i,w in enumerate(parts):
        if w.startswith("http://") or w.startswith("https://"):
            parts[i]="[ДАННЫЕ УДАЛЕНЫ]"
    return" ".join(parts)
sanitized_reports=list(map(lambda r:{"author":r["author"],"text":sanitize_text(r["text"])},reports_with_links))
print(reports_with_links)
print(sanitized_reports)


scp_objects=[{"scp":"SCP-096","class":"Euclid"},{"scp":"SCP-173","class":"Euclid"},{"scp":"SCP-055","class":"Keter"},{"scp":"SCP-999","class":"Safe"},{"scp":"SCP-3001","class":"Keter"}]
enhanced_measures=list(filter(lambda s:s["class"]!="Safe",scp_objects))
print(enhanced_measures)


incidents=[{"id":101,"staff":4},{"id":102,"staff":12},{"id":103,"staff":7},{"id":104,"staff":20}]
top_incidents=sorted(incidents,key=lambda x:x["staff"],reverse=True)[:3]
print(top_incidents)


protocols=[("Lockdown",5),("Evacuation",4),("Data Wipe",3),("Routine Scan",1)]
protocol_strings=list(map(lambda p:f"Protocol {p[0]} - Criticality {p[1]}",protocols))
print(protocol_strings)


shifts=[6,12,8,24,10,4]
valid_shifts=list(filter(lambda h:8<=h<=12,shifts))
print(valid_shifts)


evaluations=[{"name":"Agent Cole","score":78},{"name":"Dr. Weiss","score":92},{"name":"Technician Moore","score":61},{"name":"Researcher Lin","score":88}]
best=max(evaluations,key=lambda e:e["score"])
print(best["name"],best["score"])
