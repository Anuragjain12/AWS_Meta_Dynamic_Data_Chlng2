#/bin/bash
curl --silent http://169.254.169.254/latest/dynamic/instance-identity/document >> meta.json
cat meta.json
echo "\n"
echo "Enter the metadata you need from the list: accountId
architecture
availabilityZone
billingProducts
devpayProductCodes
marketplaceProductCodes
imageId
instanceId
instanceType
kernelId
pendingTime
privateIp
ramdiskId
region
version"
read filter
#echo $filter
python -c "import sys, json; print(json.load(sys.stdin)['$filter'])"  < meta.json
#jq --arg v "$filter" '.[$v]' meta.json
rm -rf meta.json