import psycopg2
import psycopg2.extras


def query(query: str):
    try:
        conn = psycopg2.connect(
            "dbname=effigo_nccltd_testing host=localhost user=postgres password=manjith")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(query=query)
        result = cur.fetchall()
        response = []
        for row in result:
            response.append(dict(row))
        return response

    finally:
        if conn is not None:
            conn.close()


def queryd(query: str):
   try:
        
        conn = psycopg2.connect(
            "dbname=effigo_nccltd_testing host=localhost user=postgres password=manjith")
        cur = conn.cursor()
        cur.execute(query=query)
        result = cur.fetchall()
        res = []
        for i in result:
            try:
                res.append({i[0]: i[1]})
            except:
                res.append(i[0])
        try:
            for j in res[1:]:
                 res[0].update(j)
        except:
            return res
        try:
            return res[0]
        except:
            return["no data"]

   finally:
       if conn is not None:
          conn.close()
