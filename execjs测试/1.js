i.onreadystatechange = function() {
            if (4 == i.readyState) {
                var a, c, f = i.status;
                if (f >= 200 && 300 > f || 304 == f) {
                    d(),
                    a = i.responseText,
                    c = i.getAllResponseHeaders() || "";
                    try {
                        a = /^\s*$/.test(a) ? {} : JSON.parse(a),
                        a.responseHeaders = c,
                        h.results = [a],
                        e.resolve()
                    } catch (g) {
                        b("PARSE_JSON_ERROR::瑙ｆ瀽JSON澶辫触")
                    }
                } else
                    d("ABORT"),
                    b(h.abortErrMsg || "ABORT::鎺ュ彛寮傚父閫€鍑�")
            }
        }