.  ./.gh-api-examples.conf

# Wrap a graphql script for use with curl

# Use a bash "here" document and shell variables will be available:

read -r -d '' graphql_script <<- EOF
{
  repository(owner: "$org", name: "$repo") {
    id
    name
    refs(refPrefix: "refs/heads/", first: 10) {
      edges {
        node {
          branchName: name
        }
      }
      pageInfo {
        endCursor
      }
      nodes {
        target {
          ... on Commit {
            committedDate
            message
          }
        }
        name
      }
    }
  }
}
EOF

# Escape quotes and reformat script to a single line
graphql_script="$(echo ${graphql_script//\"/\\\"})"


curl ${curl_custom_flags} \
     -H "Accept: application/vnd.github.v3+json" \
     -H 'Accept: application/vnd.github.audit-log-preview+json' \
     -H "Authorization: Bearer ${GITHUB_TOKEN}" \
        ${GITHUB_APIV4_BASE_URL} -d "{ \"query\": \"$graphql_script\"}"

