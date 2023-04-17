local clock = os.clock
function sleep(n)
    local t0 = clock()
    while clock() - t0 <= n do end
end

local ws, err = http.websocket("ws://localhost:3000")
if err then print(err)
elseif ws then
    while true do
        local message = ws.recieve()
        if message ~= nil then
            paintutils.drawImage(paintutils.parseImage(message),0,0)
            ws.send("update")
            sleep(0.1)
        end
    end
end
