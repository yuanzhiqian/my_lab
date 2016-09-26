local action = ngx.var.request_method;
-- important!  #这里非常重要，一开始我没有添加这行，导致没有成功发出子请求
ngx.req.read_body();

-- get request body
local data = ngx.req.get_body_data();
-- get request uri's args
local args = ngx.req.get_uri_args();

-- issue subrequest.
local res1,res2,res3 = ngx.location.capture_multi({
    {"/sub1"..ngx.var.request_uri},
    --{"/sub2"..ngx.var.request_uri},
    --{"/sub3"..ngx.var.request_uri},
    --{"/sub4"..ngx.var.request_uri},
    --{"/sub5"..ngx.var.request_uri},
    --{"/sub6"..ngx.var.request_uri},
    --{"/sub7"..ngx.var.request_uri}
    -- TODO: N's subrequests
})

ngx.say("");
