# -*- coding: utf-8 -*-

from odoo import models, fields, api

class WebsiteSocial(models.Model):
	_inherit = 'website'

	social_bitbucket = fields.Char('BitBucket Account')
	social_vimeo = fields.Char('Vimeo Account')
	social_whatsapp = fields.Char('Whatsapp Number')
	social_skype = fields.Char('Skype Account')
	social_twitch = fields.Char('Twitch Account')
	social_reddit = fields.Char('Reddit Account')
	social_tumblr = fields.Char('Tumblr Account')
	social_flickr = fields.Char('Flickr Account')
	social_pinterest = fields.Char('Pinterest Account')
	social_houzz = fields.Char('Houzz Account')

class WebsiteSocialConfig(models.TransientModel):
	_inherit = 'res.config.settings'

	social_bitbucket = fields.Char(related='website_id.social_bitbucket', readonly=False)
	social_vimeo = fields.Char(related='website_id.social_vimeo', readonly=False)
	social_whatsapp = fields.Char(related='website_id.social_whatsapp', readonly=False)
	social_skype = fields.Char(related='website_id.social_skype', readonly=False)
	social_twitch = fields.Char(related='website_id.social_twitch', readonly=False)
	social_reddit = fields.Char(related='website_id.social_reddit', readonly=False)
	social_tumblr = fields.Char(related='website_id.social_tumblr', readonly=False)
	social_flickr = fields.Char(related='website_id.social_flickr', readonly=False)
	social_pinterest = fields.Char(related='website_id.social_pinterest', readonly=False)
	social_houzz = fields.Char(related='website_id.social_houzz', readonly=False)

	@api.depends('website_id', 'social_twitter', 'social_facebook', 'social_github', 'social_linkedin', 'social_youtube', 'social_instagram', 'social_bitbucket', 'social_vimeo', 'social_whatsapp', 'social_skype', 'social_twitch', 'social_reddit', 'social_tumblr', 'social_flickr','social_pinterest','social_houzz')
	def has_social_network(self):
		self.has_social_network = self.social_twitter or self.social_facebook or self.social_github \
            or self.social_linkedin or self.social_youtube or self.social_instagram or self.social_bitbucket or self.social_vimeo \
			or self.social_whatsapp or self.social_skype or self.social_twitch \
			or self.social_reddit or self.social_tumblr or self.social_flickr \
			or self.social_pinterest or self.social_houzz

	def inverse_has_social_network(self):
		if not self.has_social_network:
			self.social_twitter = ''
			self.social_facebook = ''
			self.social_github = ''
			self.social_linkedin = ''
			self.social_youtube = ''
			self.social_instagram = ''
			self.social_bitbucket = ''
			self.social_vimeo = ''
			self.social_whatsapp = ''
			self.social_skype = ''
			self.social_twitch = ''
			self.social_reddit = ''
			self.social_tumblr = ''
			self.social_flickr = ''
			self.social_pinterest = ''
			self.social_houzz = ''

	has_social_network = fields.Boolean("Configure Social Network", compute=has_social_network, inverse=inverse_has_social_network)