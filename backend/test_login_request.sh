curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"taskname":"buy milk", "userID":"blabla"}' \
    http://localhost:5000/api/add_todo
