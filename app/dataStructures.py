tables={}
# This is a dictionary of the tables accessiable through the API
# It has not been fully sanitized with regards to permissions, so you
# Will likely run into issues where you cannot read something
# but you may be able to write to it, or visa-versa.  Basically,
# until you have worked with a specific table a couple of times,
# expect to run into errors.
tables["ActionSequence"] = ["Id",
                         "TemplateName",
                         "VisibleToTheseUsers"]
tables["AffResource"] = ["Id",
                         "Notes",
                         "ProgramIds",
                         "ResourceHREF",
                         "ResourceHTML",
                         "ResourceOrder",
                         "ResourceType",
                         "Title"]
tables["Affiliate"] = ["AffCode",
                         "AffName",
                         "ContactId",
                         "DefCommissionType",
                         "Id",
                         "LeadAmt",
                         "LeadCookieFor",
                         "LeadPercent",
                         "NotifyLead",
                         "NotifySale",
                         "ParentId",
                         "Password",
                         "PayoutType",
                         "SaleAmt",
                         "SalePercent",
                         "Status"]
tables["CCharge"] = ["Amt",
                         "ApprCode",
                         "CCId",
                         "Id",
                         "MerchantId",
                         "OrderNum",
                         "PaymentId",
                         "RefNum"]
tables["CProgram"] = ["Active",
                         "BillingType",
                         "DefaultCycle",
                         "DefaultFrequency",
                         "DefaultPrice",
                         "Description",
                         "Family",
                         "HideInStore",
                         "Id",
                         "LargeImage",
                         "ProductId",
                         "ProgramName",
                         "ShortDescription",
                         "Sku",
                         "Status",
                         "Taxable"]
tables["Campaign"] = ["Id",
                         "Name",
                         "Status"]
tables["CampaignStep"] = ["CampaignId",
                         "Id",
                         "StepStatus",
                         "StepTitle",
                         "TemplateId"]
tables["Campaignee"] = ["Campaign",
                         "CampaignId",
                         "ContactId",
                         "Status"]
tables["Company"] = ["AccountId",
                         "Address1Type",
                         "Address2Street1",
                         "Address2Street2",
                         "Address2Type",
                         "Address3Street1",
                         "Address3Street2",
                         "Address3Type",
                         "Anniversary",
                         "AssistantName",
                         "AssistantPhone",
                         "BillingInformation",
                         "Birthday",
                         "City",
                         "City2",
                         "City3",
                         "Company",
                         "CompanyID",
                         "ContactNotes",
                         "ContactType",
                         "Country",
                         "Country2",
                         "Country3",
                         "CreatedBy",
                         "DateCreated",
                         "Email",
                         "EmailAddress2",
                         "EmailAddress3",
                         "Fax1",
                         "Fax1Type",
                         "Fax2",
                         "Fax2Type",
                         "FirstName",
                         "Groups",
                         "Id",
                         "JobTitle",
                         "LastName",
                         "LastUpdated",
                         "LastUpdatedBy",
                         "MiddleName",
                         "Nickname",
                         "OwnerID",
                         "Password",
                         "Phone1",
                         "Phone1Ext",
                         "Phone1Type",
                         "Phone2",
                         "Phone2Ext",
                         "Phone2Type",
                         "Phone3",
                         "Phone3Ext",
                         "Phone3Type",
                         "Phone4",
                         "Phone4Ext",
                         "Phone4Type",
                         "Phone5",
                         "Phone5Ext",
                         "Phone5Type",
                         "PostalCode",
                         "PostalCode2",
                         "PostalCode3",
                         "ReferralCode",
                         "SpouseName",
                         "State",
                         "State2",
                         "State3",
                         "StreetAddress1",
                         "StreetAddress2",
                         "Suffix",
                         "Title",
                         "Username",
                         "Validated",
                         "Website",
                         "ZipFour1",
                         "ZipFour2",
                         "ZipFour3"]
tables["Contact"] = ["AccountId",
                         "Address1Type",
                         "Address2Street1",
                         "Address2Street2",
                         "Address2Type",
                         "Address3Street1",
                         "Address3Street2",
                         "Address3Type",
                         "Anniversary",
                         "AssistantName",
                         "AssistantPhone",
                         "BillingInformation",
                         "Birthday",
                         "City",
                         "City2",
                         "City3",
                         "Company",
                         "CompanyID",
                         "ContactNotes",
                         "ContactType",
                         "Country",
                         "Country2",
                         "Country3",
                         "CreatedBy",
                         "DateCreated",
                         "Email",
                         "EmailAddress2",
                         "EmailAddress3",
                         "Fax1",
                         "Fax1Type",
                         "Fax2",
                         "Fax2Type",
                         "FirstName",
                         "Groups",
                         "Id",
                         "JobTitle",
                         "LastName",
                         "LastUpdated",
                         "LastUpdatedBy",
                         "LeadSourceId",
                         "Leadsource",
                         "MiddleName",
                         "Nickname",
                         "OwnerID",
                         "Password",
                         "Phone1",
                         "Phone1Ext",
                         "Phone1Type",
                         "Phone2",
                         "Phone2Ext",
                         "Phone2Type",
                         "Phone3",
                         "Phone3Ext",
                         "Phone3Type",
                         "Phone4",
                         "Phone4Ext",
                         "Phone4Type",
                         "Phone5",
                         "Phone5Ext",
                         "Phone5Type",
                         "PostalCode",
                         "PostalCode2",
                         "PostalCode3",
                         "ReferralCode",
                         "SpouseName",
                         "State",
                         "State2",
                         "State3",
                         "StreetAddress1",
                         "StreetAddress2",
                         "Suffix",
                         "Title",
                         "Username",
                         "Validated",
                         "Website",
                         "ZipFour1",
                         "ZipFour2",
                         "ZipFour3"]
tables["ContactAction"] = ["Accepted",
                         "ActionDate",
                         "ActionDescription",
                         "ActionType",
                         "CompletionDate",
                         "ContactId",
                         "CreatedBy",
                         "CreationDate",
                         "CreationNotes",
                         "EndDate",
                         "Id",
                         "IsAppointment",
                         "LastUpdated",
                         "LastUpdatedBy",
                         "ObjectType",
                         "OpportunityId",
                         "PopupDate",
                         "Priority",
                         "UserID"]
tables["ContactGroup"] = ["GroupCategoryId",
                         "GroupDescription",
                         "GroupName",
                         "Id"]
tables["ContactGroupAssign"] = ["Contact.Address1Type",
                         "Contact.Address2Street1",
                         "Contact.Address2Street2",
                         "Contact.Address2Type",
                         "Contact.Address3Street1",
                         "Contact.Address3Street2",
                         "Contact.Address3Type",
                         "Contact.Anniversary",
                         "Contact.AssistantName",
                         "Contact.AssistantPhone",
                         "Contact.BillingInformation",
                         "Contact.Birthday",
                         "Contact.City",
                         "Contact.City2",
                         "Contact.City3",
                         "Contact.Company",
                         "Contact.CompanyID",
                         "Contact.ContactNotes",
                         "Contact.ContactType",
                         "Contact.Country",
                         "Contact.Country2",
                         "Contact.Country3",
                         "Contact.CreatedBy",
                         "Contact.DateCreated",
                         "Contact.Email",
                         "Contact.EmailAddress2",
                         "Contact.EmailAddress3",
                         "Contact.Fax1",
                         "Contact.Fax1Type",
                         "Contact.Fax2",
                         "Contact.Fax2Type",
                         "Contact.FirstName",
                         "Contact.Groups",
                         "Contact.Id",
                         "Contact.JobTitle",
                         "Contact.LastName",
                         "Contact.LastUpdated",
                         "Contact.LastUpdatedBy",
                         "Contact.Leadsource",
                         "Contact.MiddleName",
                         "Contact.Nickname",
                         "Contact.OwnerID",
                         "Contact.Phone1",
                         "Contact.Phone1Ext",
                         "Contact.Phone1Type",
                         "Contact.Phone2",
                         "Contact.Phone2Ext",
                         "Contact.Phone2Type",
                         "Contact.Phone3",
                         "Contact.Phone3Ext",
                         "Contact.Phone3Type",
                         "Contact.Phone4",
                         "Contact.Phone4Ext",
                         "Contact.Phone4Type",
                         "Contact.Phone5",
                         "Contact.Phone5Ext",
                         "Contact.Phone5Type",
                         "Contact.PostalCode",
                         "Contact.PostalCode2",
                         "Contact.PostalCode3",
                         "Contact.ReferralCode",
                         "Contact.SpouseName",
                         "Contact.State",
                         "Contact.State2",
                         "Contact.State3",
                         "Contact.StreetAddress1",
                         "Contact.StreetAddress2",
                         "Contact.Suffix",
                         "Contact.Title",
                         "Contact.Website",
                         "Contact.ZipFour1",
                         "Contact.ZipFour2",
                         "Contact.ZipFour3",
                         "ContactGroup",
                         "ContactId",
                         "DateCreated",
                         "GroupId"]
tables["ContactGroupCategory"] = ["CategoryDescription",
                         "CategoryName",
                         "Id"]
tables["CreditCard"] = ["BillAddress1",
                         "BillAddress2",
                         "BillCity",
                         "BillCountry",
                         "BillName",
                         "BillState",
                         "BillZip",
                         "CardType",
                         "ContactId",
                         "Email",
                         "ExpirationMonth",
                         "ExpirationYear",
                         "FirstName",
                         "Id",
                         "Last4",
                         "LastName",
                         "MaestroIssueNumber",
                         "NameOnCard",
                         "PhoneNumber",
                         "ShipAddress1",
                         "ShipAddress2",
                         "ShipCity",
                         "ShipCompanyName",
                         "ShipCountry",
                         "ShipFirstName",
                         "ShipLastName",
                         "ShipMiddleName",
                         "ShipName",
                         "ShipPhoneNumber",
                         "ShipState",
                         "ShipZip",
                         "StartDateMonth",
                         "StartDateYear",
                         "Status"]
tables["DataFormField"] = ["DataType",
                         "DefaultValue",
                         "FormId",
                         "GroupId",
                         "Id",
                         "Label",
                         "ListRows",
                         "Name",
                         "Values"]
tables["DataFormGroup"] = ["Id",
                         "Name",
                         "TabId"]
tables["DataFormTab"] = ["FormId",
                         "Id",
                         "TabName"]
tables["Expense"] = ["ContactId",
                         "DateIncurred",
                         "ExpenseAmt",
                         "ExpenseType",
                         "Id",
                         "TypeId"]
tables["FileBox"] = ["ContactId",
                         "Extension",
                         "FileName",
                         "FileSize",
                         "Id",
                         "Public"]
tables["GroupAssign"] = ["Admin",
                         "GroupId",
                         "Id",
                         "UserId"]
tables["Invoice"] = ["AffiliateId",
                         "ContactId",
                         "CreditStatus",
                         "DateCreated",
                         "Description",
                         "Id",
                         "InvoiceTotal",
                         "InvoiceType",
                         "JobId",
                         "LeadAffiliateId",
                         "PayPlanStatus",
                         "PayStatus",
                         "ProductSold",
                         "PromoCode",
                         "RefundStatus",
                         "Synced",
                         "TotalDue",
                         "TotalPaid"]
tables["InvoiceItem"] = ["CommissionStatus",
                         "DateCreated",
                         "Description",
                         "Discount",
                         "Id",
                         "InvoiceAmt",
                         "InvoiceId",
                         "OrderItemId"]
tables["InvoicePayment"] = ["Amt",
                         "Id",
                         "InvoiceId",
                         "PayDate",
                         "PayStatus",
                         "PaymentId",
                         "SkipCommission"]
tables["Job"] = ["ContactId",
                         "DateCreated",
                         "DueDate",
                         "Id",
                         "JobNotes",
                         "JobRecurringId",
                         "JobStatus",
                         "JobTitle",
                         "OrderStatus",
                         "OrderType",
                         "ProductId",
                         "StartDate"]
tables["JobRecurringInstance"] = ["AutoCharge",
                         "DateCreated",
                         "Description",
                         "EndDate",
                         "Id",
                         "InvoiceItemId",
                         "RecurringId",
                         "StartDate",
                         "Status"]
tables["Lead"] = ["AffiliateId",
                         "ContactID",
                         "CreatedBy",
                         "DateCreated",
                         "EstimatedCloseDate",
                         "Id",
                         "LastUpdated",
                         "LastUpdatedBy",
                         "Leadsource",
                         "NextActionDate",
                         "NextActionNotes",
                         "Objection",
                         "OpportunityNotes",
                         "OpportunityTitle",
                         "ProjectedRevenueHigh",
                         "ProjectedRevenueLow",
                         "StageID",
                         "StatusID",
                         "UserID"]
tables["LeadSource"] = ["CostPerLead",
                         "Description",
                         "EndDate",
                         "Id",
                         "LeadSourceCategoryId",
                         "Medium",
                         "Message",
                         "Name",
                         "StartDate",
                         "Status",
                         "Vendor"]
tables["LeadSourceCategory"] = ["Description",
                         "Id",
                         "Name"]
tables["LeadSourceExpense"] = ["Amount",
                         "DateIncurred",
                         "Id",
                         "LeadSourceId",
                         "LeadSourceRecurringExpenseId",
                         "Notes",
                         "Title"]
tables["LeadSourceRecurringExpense"] = ["Amount",
                         "EndDate",
                         "Id",
                         "LeadSourceId",
                         "NextExpenseDate",
                         "Notes",
                         "StartDate",
                         "Title"]
tables["MtgLead"] = ["ActualCloseDate",
                         "ApplicationDate",
                         "CreditReportDate",
                         "DateAppraisalDone",
                         "DateAppraisalOrdered",
                         "DateAppraisalReceived",
                         "DateRateLockExpires",
                         "DateRateLocked",
                         "DateTitleOrdered",
                         "DateTitleReceived",
                         "FundingDate",
                         "Id"]
tables["OrderItem"] = ["CPU",
                         "Id",
                         "ItemDescription",
                         "ItemName",
                         "ItemType",
                         "Notes",
                         "OrderId",
                         "PPU",
                         "ProductId",
                         "Qty",
                         "SubscriptionPlanId"]
tables["PayPlan"] = ["AmtDue",
                         "DateDue",
                         "FirstPayAmt",
                         "Id",
                         "InitDate",
                         "InvoiceId",
                         "StartDate",
                         "Type"]
tables["PayPlanItem"] = ["AmtDue",
                         "AmtPaid",
                         "DateDue",
                         "Id",
                         "PayPlanId",
                         "Status"]
tables["Payment"] = ["ChargeId",
                         "Commission",
                         "ContactId",
                         "Id",
                         "InvoiceId",
                         "PayAmt",
                         "PayDate",
                         "PayNote",
                         "PayType",
                         "RefundId",
                         "Synced",
                         "UserId"]
tables["Product"] = ["BottomHTML",
                         "CityTaxable",
                         "CountryTaxable",
                         "Description",
                         "HideInStore",
                         "Id",
                         "InventoryLimit",
                         "InventoryNotifiee",
                         "IsPackage",
                         "LargeImage",
                         "NeedsDigitalDelivery",
                         "ProductName",
                         "ProductPrice",
                         "Shippable",
                         "ShippingTime",
                         "ShortDescription",
                         "Sku",
                         "StateTaxable",
                         "Status",
                         "Taxable",
                         "TopHTML",
                         "Weight"]
tables["ProductCategory"] = ["CategoryDisplayName",
                         "CategoryImage",
                         "CategoryOrder",
                         "Id",
                         "ParentId"]
tables["ProductCategoryAssign"] = ["Id",
                         "ProductCategoryId",
                         "ProductId"]
tables["ProductInterest"] = ["DiscountPercent",
                         "Id",
                         "ObjType",
                         "ObjectId",
                         "ProductId",
                         "ProductType",
                         "Qty"]
tables["ProductInterestBundle"] = ["BundleName",
                         "Description",
                         "Id"]
tables["ProductOptValue"] = ["Id",
                         "IsDefault",
                         "Label",
                         "Name",
                         "OptionIndex",
                         "PriceAdjustment",
                         "ProductOptionId",
                         "Sku"]
tables["ProductOption"] = ["AllowSpaces",
                         "CanContain",
                         "CanEndWith",
                         "CanStartWith",
                         "Id",
                         "IsRequired",
                         "Label",
                         "MaxChars",
                         "MinChars",
                         "Name",
                         "OptionType",
                         "Order",
                         "ProductId",
                         "TextMessage"]
tables["RecurringOrder"] = ["AffiliateId",
                         "AutoCharge",
                         "BillingAmt",
                         "BillingCycle",
                         "CC1",
                         "CC2",
                         "ContactId",
                         "EndDate",
                         "Frequency",
                         "Id",
                         "LastBillDate",
                         "LeadAffiliateId",
                         "MaxRetry",
                         "MerchantAccountId",
                         "NextBillDate",
                         "NumDaysBetweenRetry",
                         "OriginatingOrderId",
                         "PaidThruDate",
                         "ProductId",
                         "ProgramId",
                         "PromoCode",
                         "Qty",
                         "ReasonStopped",
                         "ShippingOptionId",
                         "StartDate",
                         "Status",
                         "SubscriptionPlanId"]
tables["RecurringOrderWithContact"] = ["AffiliateId",
                         "AutoCharge",
                         "BillingAmt",
                         "BillingCycle",
                         "CC1",
                         "CC2",
                         "City",
                         "ContactId",
                         "ContactId",
                         "Country",
                         "Email",
                         "EmailAddress2",
                         "EmailAddress3",
                         "EndDate",
                         "FirstName",
                         "Frequency",
                         "LastBillDate",
                         "LastName",
                         "LeadAffiliateId",
                         "MaxRetry",
                         "MerchantAccountId",
                         "MiddleName",
                         "NextBillDate",
                         "Nickname",
                         "NumDaysBetweenRetry",
                         "PaidThruDate",
                         "Phone1",
                         "Phone1Ext",
                         "Phone1Type",
                         "Phone2",
                         "Phone2Ext",
                         "Phone2Type",
                         "PostalCode",
                         "ProductId",
                         "ProgramId",
                         "PromoCode",
                         "Qty",
                         "ReasonStopped",
                         "RecurringOrderId",
                         "ShippingOptionId",
                         "SpouseName",
                         "StartDate",
                         "State",
                         "Status",
                         "StreetAddress1",
                         "StreetAddress2",
                         "SubscriptionPlanId",
                         "Suffix",
                         "Title",
                         "ZipFour1"]
tables["Referral"] = ["AffiliateId",
                         "ContactId",
                         "DateExpires",
                         "DateSet",
                         "IPAddress",
                         "Id",
                         "Info",
                         "Source",
                         "Type"]
tables["SavedFilter"] = ["FilterName",
                         "Id",
                         "ReportStoredName",
                         "UserId"]
tables["Stage"] = ["Id",
                         "StageName",
                         "StageOrder",
                         "TargetNumDays"]
tables["StageMove"] = ["CreatedBy",
                         "DateCreated",
                         "Id",
                         "MoveDate",
                         "MoveFromStage",
                         "MoveToStage",
                         "OpportunityId",
                         "PrevStageMoveDate",
                         "UserId"]
tables["Status"] = ["Id",
                         "StatusName",
                         "StatusOrder",
                         "TargetNumDays"]
tables["SubscriptionPlan"] = ["Active",
                         "Cycle",
                         "Frequency",
                         "Id",
                         "PlanPrice",
                         "PreAuthorizeAmount",
                         "ProductId",
                         "Prorate"]
tables["Template"] = ["Categories",
                         "Id",
                         "PieceTitle",
                         "PieceType"]
tables["TicketStage"] = ["Id",
                         "StageName"]
tables["TicketType"] = ["CategoryId",
                         "Id",
                         "Label"]
tables["User"] = ["City",
                         "Email",
                         "EmailAddress2",
                         "EmailAddress3",
                         "FirstName",
                         "HTMLSignature",
                         "Id",
                         "LastName",
                         "MiddleName",
                         "Nickname",
                         "Phone1",
                         "Phone1Ext",
                         "Phone1Type",
                         "Phone2",
                         "Phone2Ext",
                         "Phone2Type",
                         "PostalCode",
                         "Signature",
                         "SpouseName",
                         "State",
                         "StreetAddress1",
                         "StreetAddress2",
                         "Suffix",
                         "Title",
                         "ZipFour1"]
tables["UserGroup"] = ["Id",
                         "Name",
                         "OwnerId"]
