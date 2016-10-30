USE [zm]
GO

/****** Object:  Table [dbo].[zmA]    Script Date: 2016-10-31 오전 1:25:07 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[zmA](
	[zm_id] [int] IDENTITY(1,1) NOT NULL,
	[zm_date] [date] NULL,
	[grade] [int] NULL,
	[code] [varchar](10) NULL,
	[mesur] [float] NULL,
	[medor] [float] NULL,
	[msr_mdr] [float] NULL,
	[smesur] [float] NULL,
	[smedor] [float] NULL,
	[smsr_mdr] [float] NULL,
	[sgrad] [float] NULL,
	[ssd] [float] NULL,
	[grad] [float] NULL,
	[sd] [float] NULL,
	[second] [float] NULL,
	[srgrad] [float] NULL,
	[srsd] [float] NULL,
	[rgrad] [float] NULL,
	[rsd] [float] NULL,
	[gr] [float] NULL,
	[mesu] [float] NULL,
	[maxc_msc] [float] NULL,
	[X3c_msc] [float] NULL,
	[X5c_msc] [float] NULL,
	[X7c_msc] [float] NULL,
	[X10c_msc] [float] NULL,
	[X15c_msc] [float] NULL,
	[X20c_msc] [float] NULL,
	[X30c_msc] [float] NULL,
	[msc_min10c] [float] NULL,
	[msc_min20c] [float] NULL,
	[msc_min30c] [float] NULL,
	[max] [float] NULL,
	[min] [float] NULL,
	[cost] [float] NULL,
	[mult] [float] NULL,
	[mult2] [float] NULL,
	[ud] [varchar](10) NULL,
	[ud2] [varchar](10) NULL,
	[ud3] [varchar](10) NULL,
	[udm] [varchar](10) NULL,
	[udm2] [varchar](10) NULL
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


