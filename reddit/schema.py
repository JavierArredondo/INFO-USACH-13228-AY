SCHEMA = {
  "name": "MyClass",
  "type": "record",
  "namespace": "com.acme.avro",
  "fields": [
    {
      "name": "all_awardings",
      "type": {
        "type": "array"
      }
    },
    {
      "name": "allow_live_comments",
      "type": "boolean"
    },
    {
      "name": "approved_at_utc",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "approved_by",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "archived",
      "type": "boolean"
    },
    {
      "name": "author",
      "type": "string"
    },
    {
      "name": "author_flair_background_color",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "author_flair_css_class",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "author_flair_richtext",
      "type": {
        "type": "array"
      }
    },
    {
      "name": "author_flair_template_id",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "author_flair_text",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "author_flair_text_color",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "author_flair_type",
      "type": "string"
    },
    {
      "name": "author_fullname",
      "type": "string"
    },
    {
      "name": "author_patreon_flair",
      "type": "boolean"
    },
    {
      "name": "author_premium",
      "type": "boolean"
    },
    {
      "name": "awarders",
      "type": {
        "type": "array"
      }
    },
    {
      "name": "banned_at_utc",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "banned_by",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "can_gild",
      "type": "boolean"
    },
    {
      "name": "can_mod_post",
      "type": "boolean"
    },
    {
      "name": "category",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "clicked",
      "type": "boolean"
    },
    {
      "name": "content_categories",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "contest_mode",
      "type": "boolean"
    },
    {
      "name": "created",
      "type": "int"
    },
    {
      "name": "created_utc",
      "type": "int"
    },
    {
      "name": "discussion_type",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "distinguished",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "domain",
      "type": "string"
    },
    {
      "name": "downs",
      "type": "int"
    },
    {
      "name": "edited",
      "type": "boolean"
    },
    {
      "name": "gilded",
      "type": "int"
    },
    {
      "name": "gildings",
      "type": {
        "name": "gildings",
        "type": "record",
        "fields": []
      }
    },
    {
      "name": "hidden",
      "type": "boolean"
    },
    {
      "name": "hide_score",
      "type": "boolean"
    },
    {
      "name": "id",
      "type": "string"
    },
    {
      "name": "is_crosspostable",
      "type": "boolean"
    },
    {
      "name": "is_meta",
      "type": "boolean"
    },
    {
      "name": "is_original_content",
      "type": "boolean"
    },
    {
      "name": "is_reddit_media_domain",
      "type": "boolean"
    },
    {
      "name": "is_robot_indexable",
      "type": "boolean"
    },
    {
      "name": "is_self",
      "type": "boolean"
    },
    {
      "name": "is_video",
      "type": "boolean"
    },
    {
      "name": "likes",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "link_flair_background_color",
      "type": "string"
    },
    {
      "name": "link_flair_css_class",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "link_flair_richtext",
      "type": {
        "type": "array"
      }
    },
    {
      "name": "link_flair_text",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "link_flair_text_color",
      "type": "string"
    },
    {
      "name": "link_flair_type",
      "type": "string"
    },
    {
      "name": "locked",
      "type": "boolean"
    },
    {
      "name": "media",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "media_embed",
      "type": {
        "name": "media_embed",
        "type": "record",
        "fields": []
      }
    },
    {
      "name": "media_only",
      "type": "boolean"
    },
    {
      "name": "mod_note",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "mod_reason_by",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "mod_reason_title",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "mod_reports",
      "type": {
        "type": "array"
      }
    },
    {
      "name": "name",
      "type": "string"
    },
    {
      "name": "no_follow",
      "type": "boolean"
    },
    {
      "name": "num_comments",
      "type": "int"
    },
    {
      "name": "num_crossposts",
      "type": "int"
    },
    {
      "name": "num_reports",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "over_18",
      "type": "boolean"
    },
    {
      "name": "parent_whitelist_status",
      "type": "string"
    },
    {
      "name": "permalink",
      "type": "string"
    },
    {
      "name": "pinned",
      "type": "boolean"
    },
    {
      "name": "post_hint",
      "type": "string"
    },
    {
      "name": "preview",
      "type": {
        "name": "preview",
        "type": "record",
        "fields": [
          {
            "name": "enabled",
            "type": "boolean"
          },
          {
            "name": "images",
            "type": {
              "type": "array",
              "items": {
                "name": "images_record",
                "type": "record",
                "fields": [
                  {
                    "name": "id",
                    "type": "string"
                  },
                  {
                    "name": "resolutions",
                    "type": {
                      "type": "array",
                      "items": [
                        [
                          [
                            {
                              "name": "resolutions_record",
                              "type": "record",
                              "fields": [
                                {
                                  "name": "height",
                                  "type": "int"
                                },
                                {
                                  "name": "url",
                                  "type": "string"
                                },
                                {
                                  "name": "width",
                                  "type": "int"
                                }
                              ]
                            },
                            {
                              "name": "resolutions_record",
                              "type": "record",
                              "fields": [
                                {
                                  "name": "height",
                                  "type": "int"
                                },
                                {
                                  "name": "url",
                                  "type": "string"
                                },
                                {
                                  "name": "width",
                                  "type": "int"
                                }
                              ]
                            }
                          ],
                          {
                            "name": "resolutions_record",
                            "type": "record",
                            "fields": [
                              {
                                "name": "height",
                                "type": "int"
                              },
                              {
                                "name": "url",
                                "type": "string"
                              },
                              {
                                "name": "width",
                                "type": "int"
                              }
                            ]
                          }
                        ],
                        {
                          "name": "resolutions_record",
                          "type": "record",
                          "fields": [
                            {
                              "name": "height",
                              "type": "int"
                            },
                            {
                              "name": "url",
                              "type": "string"
                            },
                            {
                              "name": "width",
                              "type": "int"
                            }
                          ]
                        }
                      ]
                    }
                  },
                  {
                    "name": "source",
                    "type": {
                      "name": "source",
                      "type": "record",
                      "fields": [
                        {
                          "name": "height",
                          "type": "int"
                        },
                        {
                          "name": "url",
                          "type": "string"
                        },
                        {
                          "name": "width",
                          "type": "int"
                        }
                      ]
                    }
                  },
                  {
                    "name": "variants",
                    "type": {
                      "name": "variants",
                      "type": "record",
                      "fields": []
                    }
                  }
                ]
              }
            }
          }
        ]
      }
    },
    {
      "name": "pwls",
      "type": "int"
    },
    {
      "name": "quarantine",
      "type": "boolean"
    },
    {
      "name": "removal_reason",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "removed_by",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "removed_by_category",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "report_reasons",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "retrieved_on",
      "type": "int"
    },
    {
      "name": "saved",
      "type": "boolean"
    },
    {
      "name": "score",
      "type": "int"
    },
    {
      "name": "secure_media",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "secure_media_embed",
      "type": {
        "name": "secure_media_embed",
        "type": "record",
        "fields": []
      }
    },
    {
      "name": "selftext",
      "type": "string"
    },
    {
      "name": "selftext_html",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "send_replies",
      "type": "boolean"
    },
    {
      "name": "spoiler",
      "type": "boolean"
    },
    {
      "name": "stickied",
      "type": "boolean"
    },
    {
      "name": "subreddit",
      "type": "string"
    },
    {
      "name": "subreddit_id",
      "type": "string"
    },
    {
      "name": "subreddit_name_prefixed",
      "type": "string"
    },
    {
      "name": "subreddit_subscribers",
      "type": "int"
    },
    {
      "name": "subreddit_type",
      "type": "string"
    },
    {
      "name": "suggested_sort",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "thumbnail",
      "type": "string"
    },
    {
      "name": "thumbnail_height",
      "type": "int"
    },
    {
      "name": "thumbnail_width",
      "type": "int"
    },
    {
      "name": "title",
      "type": "string"
    },
    {
      "name": "top_awarded_type",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "total_awards_received",
      "type": "int"
    },
    {
      "name": "treatment_tags",
      "type": {
        "type": "array"
      }
    },
    {
      "name": "ups",
      "type": "int"
    },
    {
      "name": "upvote_ratio",
      "type": "float"
    },
    {
      "name": "url",
      "type": "string"
    },
    {
      "name": "url_overridden_by_dest",
      "type": "string"
    },
    {
      "name": "user_reports",
      "type": {
        "type": "array"
      }
    },
    {
      "name": "view_count",
      "type": [
        "string",
        "null"
      ]
    },
    {
      "name": "visited",
      "type": "boolean"
    },
    {
      "name": "whitelist_status",
      "type": "string"
    },
    {
      "name": "wls",
      "type": "int"
    }
  ]
}