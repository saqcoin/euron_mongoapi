# mongo Db
mongodb+srv://saqrsh_db_user:ir1starQ@testcluster.sb8lqib.mongodb.net/?appName=testCluster

python -m pip install "pymongo[srv]"

saqrsh_db_user : ir1starQ

Collection is euivalent to SQL tables

async await --> async is a non blocking function so await waits for the response for the function --> used for high traffic api
motor is created by mongo for making asynchronous api

echo "# euron_mongoapi" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/saqcoin/euron_mongoapi.git
git push -u origin main

push code to github or any platform

then use render for hosting the api

deployed to https://squ-euron-mongoapi.onrender.com


MongoDB
pymongo.errors.ServerSelectionTimeoutError: SSL handshake failed
https://www.mongodb.com/community/forums/t/pymongo-errors-serverselectiontimeouterror-ssl-handshake-failed/150205
02 Mar 2022 — That error is usually due to a configuration issue in MongoDB Atlas. When you connect from your localhost, there's no problem because MongoDB Atlas configures ...See more

{
  "message": "data deleted for DeleteResult({'n': 1, 'electionId': ObjectId('7fffffff0000000000000057'), 'opTime': {'ts': Timestamp(1763583283, 6), 't': 87}, 'ok': 1.0, '$clusterTime': {'clusterTime': Timestamp(1763583283, 6), 'signature': {'hash': b'\\xb1\\x16\\x03c\\xb8R\\x81\\x91Ds%\\xd5\\x11\\xcc\\xa5\\xd2\\x91\\xcb\\xf8Y', 'keyId': 7522907962252197890}}, 'operationTime': Timestamp(1763583283, 6)}, acknowledged=True)"
}
{
  "message": "data deleted for DeleteResult({'n': 0, 'electionId': ObjectId('7fffffff0000000000000057'), 'opTime': {'ts': Timestamp(1763583366, 1), 't': 87}, 'ok': 1.0, '$clusterTime': {'clusterTime': Timestamp(1763583366, 1), 'signature': {'hash': b'\\xfcg\\xfas1\\x17\\x05O(\\xd8\\xdb\\x14\\xc4\\xd6\\xb0\\xda\\x04\\xb2\\xfc\\xf5', 'keyId': 7522907962252197890}}, 'operationTime': Timestamp(1763583366, 1)}, acknowledged=True)"
}


fastapi converts the inputs to the types you've defined. in this case, AssessmentQNASortOrder. class members are accessed with the dot notation:

assessment_qna.sort_order