.  ./.gh-api-examples.conf

# https://docs.github.com/en/rest/reference/pulls#get-a-pull-request
# GET /repos/:owner/:repo/pulls/:pull_number

pull=2

curl ${curl_custom_flags} \
     -H "Accept: application/vnd.github.v3+json" \
     -H "Authorization: Bearer ${GITHUB_TOKEN}" \
        ${GITHUB_API_BASE_URL}/repos/${org}/${repo}/pulls/${pull}
